export interface IChatItem {
  by: "user" | "arona",
  content: string,
  hash: number,
}

export interface IMollufyOptions {
  ignoreNounLengthLimit: boolean,
  changeMolluMark: boolean,
  forceMollufyForPredefinedWords: boolean,
}

export interface IStoreState {
  appVersion: string,
  gaEnabled: boolean,

  enableMolluImageAnimation: boolean,
  mollufyOptions: IMollufyOptions,
}
